// npm install aws-sdk

import AWS from 'aws-sdk';

AWS.config.update({
  accessKeyId: '',
  secretAccessKey: '', //Private key and access key temporarily omitted until AWS can be properly configured in the backend rather than front.
  region: 'us-west-2'
});

const ses = new AWS.SES({ apiVersion: '2010-12-01' });


export function sendEmail(recipient, subject, message) {
    const params = {
      Destination: {
        ToAddresses: [recipient]
      },
      Message: {
        Body: {
          Text: {
            Data: message
          }
        },
        Subject: {
          Data: subject
        }
      },
      Source: 'WolfCampus <clintv@nevada.unr.edu>' 
    };
  
    return new Promise((resolve, reject) => {
      ses.sendEmail(params, (err, data) => {
        if (err) {
          reject(err);
        } else {
          resolve(data);
        }
      });
    });
  }
