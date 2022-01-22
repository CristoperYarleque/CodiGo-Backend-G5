import express,{json} from "express"
import cors from "cors"

const app = express()

const productos = [{
    nombre:"leche de almendras",
    precio:9.5,
    estado:true
}]

app.use(json())
app.use(cors())

const port = 3000

app.get('/',(req,res) => {
    res.status(200).json({
        message: 'Peticion realizada exitosamente',
    })
})

app.post('/producto',(req,res) => {
    console.log(req.body)
    if(req.body){
        productos.push(req.body)
        res.status(201).json({
            message: 'producto agregado exitosamente',
            producto: req.body, 
        })
    }else{
        res.status(400).json({
            message:"informacion incorrecta"
        })
    } 
})

app.get("/productos",(req,res) => {
    res.status(200).json({
        message:"Los productos son:",
        content: productos
    })
})

app
.route("/producto/:id")
.get((req,res) => {
    const {id} = req.params
    if(productos[id]){
        return res.status(200).json({
            message:"Producto existe",
            content: productos[id]
        })
    }else{
        return res.status(400).json({
            message:"Producto no existe",
            content: null
        })
    }
})
.put((req,res) => {
    const {id} = req.params
    if(productos[id]){
        productos[id] = req.body
        return res.status(200).json({
            message:"Producto actualizado exitosamente",
            content: productos[id]
        })
    }else{
        return res.status(400).json({
            message:"No se pudo actualizar",
            content: null
        })
    }
})
.delete((req,res)=> {
    const {id} = req.params
    if(productos[id]){
        const producto = productos[id]
        productos.splice(id, 1)
        return res.status(200).json({
            message:"Producto eliminado exitosamente",
            content: producto,
        })
    }else{
        return res.status(400).json({
            message:"No se pudo eliminar",
            content:null
        })
    }
})

app.listen(port,() => {
    console.log(`servidor levantado exitosamente! ${port}`)
})
