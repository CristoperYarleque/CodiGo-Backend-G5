import express from "express"
import prisma from "@prisma/client"
const {PrismaClient} = prisma

const app = express()
const PORT = process.env.PORT ?? 3000



app.listen(PORT, () =>{
    console.log(`Servidor corriendo exitosamente 🚀 en el puerto ${PORT}`)
})