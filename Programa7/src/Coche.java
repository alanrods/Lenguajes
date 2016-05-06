
public class Coche extends Vehiculo {
    /*En esta clase se muestra como se realiza la eleccion y encadenamiendo de constructores*/
    /*Dependiendo de los argumentos que reciba escogera el constructor indicado */
    String colorDeCoche;
    int numeroDePlacas;

    public Coche(){
    }

    public Coche(String marca){
        /*Constructor chaining from the subclass to the superclass*/
        super(marca);
    }
    public Coche(String marca, int placas){
        this(marca);
        this.numeroDePlacas = placas;
    }

    public Coche(String marca, int placas, String color){
        this(marca, placas);
        this.colorDeCoche = color;
    }

    public String toString(){
        return super.toString()+ " Placas: " + numeroDePlacas + " Color: " + colorDeCoche;
    }
}
