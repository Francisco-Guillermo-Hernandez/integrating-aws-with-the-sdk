import {PollyClient, SynthesizeSpeechCommand, SynthesizeSpeechCommandInput, VoiceId} from '@aws-sdk/client-polly';
import {S3Client} from '@aws-sdk/client-s3';
import {Upload} from '@aws-sdk/lib-storage';

const region = 'us-east-2';
const bucketName = 'polly-audio-storage-tts';

const polly = new PollyClient({ region });
const s3 = new S3Client({ region });

type EventData = {
    text: string;
}

export const handler = async (event: EventData) => {
    try {
        const text = event?.text;
        const voice = VoiceId.Salli;

        if (text && text.length > 5) {
            const params: SynthesizeSpeechCommandInput = {
                Text: text,
                OutputFormat: 'mp3',
                VoiceId: voice,
            };

            const command= new SynthesizeSpeechCommand(params);
            const data = await polly.send(command);
            const key = `audio-${Date.now()}.mp3`;

            const s3Params = {
                Bucket: bucketName,
                Key: key,
                Body: data.AudioStream,
                ContentType: 'audio/mpeg'
            };

            const upload = new Upload({
                client: s3,
                params: s3Params,
            });

            await upload.done();
            const outputMessage = `The audio file has been successfully stored in the S3 bucket by the name ${key}`;

            return {
                statusCode: 200,
                body: { message: outputMessage }
            };
        } else {
            return {
                statusCode: 400,
                body: { message: 'Please provide a valid text' }
            }
        }

    } catch (e) {
        console.log(e);
        return {
            statusCode: 500,
            body: { message: 'Internal Server Error' }
        }
    }
}