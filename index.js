import express from "express"

const app = express()
const port = 3000

app.get('/',(req,res) => {
    res.status(200).json({
        message: 'Peticion realizada exitosamente',
    })
})

app.listen(port,() => {
    console.log(`servidor levantado exitosamente! ${port}`)
})



