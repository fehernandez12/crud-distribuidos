import firebase_admin
from firebase_admin import credentials, firestore

certs = {
    "type": "service_account",
    "project_id": "crud-distribuidos-84afa",
    "private_key_id": "55c2402da3bce94bd077f12633d003ea828e272b",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDWd5O5TyCier/l\nmv526f7k3Mt9hm3jMbQUga0ltRHQU2A+9p14gr1DKaez1l0yAp0kW0Npn0jfGazM\nv5zDwqd3rMF/Xwn+TxmKQP/E3ixPqT0roNOrhW2ucAOTQbHoa+293KhhBYb1zufl\ntj8QuG9PAwDB0GwdSFqefFqcw2MtFFPlP7BldXizrLoqscY9f63Oit90+EIPFbCr\nVhll2LLYFMQ3UF9hvfMkScTPMkBeqVhvoGuJt01h8ErIDX+M37jPm0pNVPFGz/hX\nhr8i84BNibSyqIcR29Rth84ylZ31w8KnZl+2gVoqWNpx9uTFUpFxWLIP/0lpCpFO\nGEu8gEg3AgMBAAECggEAQeC7RMnUiXRRK9M/ZQGdpWlZLHa1nHsxCLeImzOShD6I\nKu8QEet+/Xl3JRusxubcpEVQYMpn1PgLB124Zr2NOYqcaWalKDPd8YTjy/I/BD1F\nJ/if7Gjw9ws7XelpH66/eXmlUyAig7EJtJsVpioxLsEKY36FJz2JcHNcVhkCht7O\noCy+iTJDGo12u6e9W188B7rzzovaIsuLdnacwIuZu5zvLq1zdpS3PToQEwTTHkag\nDKjM7b5FO1aQugOunHFUzt4+pk4NPP+Iedz9diCqUdibUIj9dtpXeLvfQjcfkUTk\nqpbhApMTwYM+bqHklo7ofXXztssBu7ANO/XYYEPMeQKBgQDxCW+qP5tXCjsdCRte\nUbtHG/XLDtQZaqx/5NLpPKsSGix6kqnpmzM4ntZgOlOvdl0BKZwAswkG/0HnT279\njXwsdmj/IGtb4BI0/g+sp5PX/y6ONqi5hwgZyIeaTPk7Mwi2a6FS+HQzIljDmG+s\nVeQu7QheznHNwkNIHsQ26bxLhQKBgQDjx+S+QtYFKoYcB5ntpf7uWN2/swsi5hWC\n5lqoQWLoSIYRAgVc8H32m8PFeBR+7/t75N0Qer/JQhDAXz6AXkgaNqT945d6RqWv\nMD6OFjkvCHdKVLnmMHOwOoT6WktlVlCcGqlE1HuHfiA2XQCI9uVcmVDu8y7jtBU2\n//UsGy9biwKBgE/shBVcwAKNhupq0aNl0IaUs9zgDt5aq9ZAptrl3gfDnAoMxcCL\nUOGucYE49fTRd6diB7OHqi+ixlSP10rF9m272bb3JgIx+3eM4t+qNXDC0cogP7Q9\nHSeHgcddTKsfkf0DFVwwvD8UXYCF9EmdtWsF9+eP5taGWs74PLHEsUYNAoGBALQN\nxg5zzLQGuj4b8ByAM/V6v8cSI8JxeB2iM5V/Ik0VTwzQuSaPYDL5TBajZig1UWjN\nL8YgEcxocc9vOnvEi2BVQ7UCHDJm9/90tm4guREpswpJ0S1ZrYlnqMgxahnv0gaj\nuJwVDpS7KYFvoMWjzQiWlPhduPn71y1DxS0ZTCUjAoGBAMlmo4ZDVZ1zfj5CbaDk\nevGF7TH2gbuwuDlWujgc/PoQziNc3l4h2R7U6JFaJSQQW5+hT63WJFpZ7CuKnmcx\nCtsTpZrqbM0ZmtqF/sna1qcWNI9ntYC8PYOmyHGKExf13WuNxRrh8e/xdxKBjo18\nqkev73ps11IEs4eq475aWVJe\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-8u68m@crud-distribuidos-84afa.iam.gserviceaccount.com",
    "client_id": "116946983345524489535",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-8u68m%40crud-distribuidos-84afa.iam.gserviceaccount.com"
}

cred = credentials.Certificate(certs)
app = firebase_admin.initialize_app(cred)
database = firestore.client(app)