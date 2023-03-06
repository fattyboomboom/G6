// import axios from 'axios';

export default class ErrorService {
  static getErrorMessage(errorCode) {
    switch(errorCode) {
      case 403:
        return 'Profanity found in post';
      case 406:
        return 'Please enter submission!';
      case 200:
        return 'Post uploaded!';
    }
  }
}
