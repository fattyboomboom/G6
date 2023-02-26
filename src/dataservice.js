import http from "@/main";

class SignUpsService {
    create(data) {
        return http.post("/register", data)
    }
}

export default new SignUpService();