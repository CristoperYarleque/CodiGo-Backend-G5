import { Usuario } from "../models/usuario.model.js";
import { hashSync } from "bcrypt";
import cryptojs from "crypto-js";
import sgMail from "@sendgrid/mail";

export class usuarioService {
  static async registro(data) {
    try {
      const password = hashSync(data.password, 10);
      const usuarioCreado = await Usuario.create({ ...data, password });
      return usuarioCreado;
    } catch (error) {
      return { message: "Error al crear el usuario", content: error.message };
    }
  }
  static async olvidePassword(correo) {
    const usuarioEncontrado = await Usuario.findOne({ usuarioCorreo: correo });
    if (usuarioEncontrado) {
      const token = cryptojs.AES.encrypt(
        JSON.stringify({
          correo: usuarioEncontrado.usuarioCorreo,
          nombre: usuarioEncontrado.usuarioNombre,
        }),
        process.env.SECRET_CRYPT_PASSWORD
      ).toString();
      await sgMail.send({
        from: "caypsaturno@gmail.com",
        text: `Ups parece que has olvidado la contrasena, ingresa a este link para restaurar la contrasen http://localhost:3000?token=${token}`,
        subject: "Restauracion de la contrasena",
        to: usuarioEncontrado.usuarioCorreo,
        html: `
        <h2>Hola has olvidado la contrasena?</h2>
        <p>Ingresa al siguiente link para restaurarla</p>
        <code>http://localhost:3000?token=${token}</code>
        `,
      });
    }
  }
  static async resetPassword(hash, password) {
    const tokenDecodificada = JSON.parse(
      cryptojs.AES.decrypt(token, process.env.SECRET_CRYPT_PASSWORD).toString(
        cryptojs.enc.Utf8
      )
    );
  }
}
