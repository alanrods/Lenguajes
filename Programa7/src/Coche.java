/**
 * Ayuda a ejemplificar elección y encadenamiento de constructores
 * Dependiendo de los argumentos que reciba escogera el constructor adecuado
 * 05/05/2016
 */ 
public class Coche extends Vehiculo {
    
    String colorDeCoche;
    int numeroDePlacas;

/**
 * Constructor por defecto 
 */
    public Coche(){
    }

/**
 * Constructor de encadenamiento de la subclase con la superclase
 * @param marca del vehículo
 */
    public Coche(String marca){
        super(marca);
    }

/**
 * Constructor de encadenamiento 
 * @param marca que se asigna en superclase y placas que se asigna a un atributo en la subclase
 */
    public Coche(String marca, int placas){
        this(marca);
        this.numeroDePlacas = placas;
    }

/**
 * Constructor de encadenamiento 
 * @param marca que se asigna en superclase,placas y color que se asignan a atributos en la subclase 
 */
    public Coche(String marca, int placas, String color){
        this(marca, placas);
        this.colorDeCoche = color;
    }
/**
 * Indica las características del vehículo
 * @return Devuelve todas las característica del vehiculo
 */
    public String toString(){
        return super.toString()+ " Placas: " + numeroDePlacas + " Color: " + colorDeCoche;
    }
}
