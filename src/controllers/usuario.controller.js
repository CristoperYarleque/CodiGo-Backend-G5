import { usuarioDto } from "../dto/request/usuario.dto.js";
import { usuarioService } from "../services/usuario.service.js";

export async function crearUsuario(req, res) {
  try {
    const data = usuarioDto(req.body);
    const resultado = await usuarioService.registro(data);
    if (resultado.message) {
      return res.status(400).json(resultado);
    } else {
      return res.status(201).json(resultado);
    }
  } catch (error) {
    return res.status(400).json({
      message: "Error al registrar el usuario",
      content: error.message,
    });
  }
}

export async function olvidePassword(req, res) {
  const resultado = await usuarioService.olvidePassword(req.body.correo);
  return res.status(204).send();
}
