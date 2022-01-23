import express, {json} from "express"
import { categoriaRouter } from "./routes/categoria.routes.js"

const app = express()
const PORT = process.env.PORT ?? 3000

// declarar el tipo de contenido
app.use(json())
// declaramos las rutas
app.use(categoriaRouter)

app.listen(PORT, () =>{
    console.log(`Servidor corriendo exitosamente 🚀 en el puerto ${PORT}`)
})

