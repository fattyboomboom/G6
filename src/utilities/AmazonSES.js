// npm install aws-sdk

import AWS from 'aws-sdk';

AWS.config.update({
  accessKeyId: 'AKIAZ6IIAQRWTCGQQWEA',
  secretAccessKey: '', //PrivateKey temporarily omitted until AWS can be properly configured in the backend rather than front.
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









//////// // npm install aws-sdk

// import AWS from 'aws-sdk';

// AWS.config.update({
//   accessKeyId: 'AKIAZ6IIAQRWTCGQQWEA',
//   secretAccessKey: 'R1+MVSPmeoLuo0YdCvUy7N/xMEHfdAzmu0WiSYZO',
//   region: 'us-east-1' // replace with your desired region
// });

// const ses = new AWS.SES({ apiVersion: '2010-12-01' });


// export function sendEmail(recipient, subject, message) {
//     const params = {
//       Destination: {
//         ToAddresses: [recipient]
//       },
//       Message: {
//         Body: {
//           Text: {
//             Data: message
//           }
//         },
//         Subject: {
//           Data: subject
//         }
//       },
//       Source: 'clintv@nevada.unr.edu' // replace with the sender's email address
//     };
  
//     return new Promise((resolve, reject) => {
//       ses.sendEmail(params, (err, data) => {
//         if (err) {
//           console.error(err);
//           reject(err.message);
//         } else {
//           resolve(data);
//         }
//       });
//     });
//   }