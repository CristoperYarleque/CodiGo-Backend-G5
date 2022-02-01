import { prisma } from "../prisma.js";

export class AuthService {
  static async login({ correo, password }) {
    const usuarioEncontrado = await prisma.usuario.findUnique({
      where: { correo },
      select: { password: true, tipoUsuario: true },
      rejectOnNotFound: true,
    });
    return { message: "Si existe" };
  }
}
