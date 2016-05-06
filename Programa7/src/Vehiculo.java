/**
 * Ejemplifica la elección de constructores
 * 05/05/2016
 */
public class Vehiculo {
    private static final int SPEED = 250;
    private String marcaVehiculo;
    private int mymaxSpeed = 350;

/**
 * Constructor por default, sin parámetros.Indica que el vehículo no tiene marca
 */ 
    public Vehiculo(){
        this.marcaVehiculo = "Sin Marca";
    }
/**
 * Constructor que asigna una marca dada al vehículo
 * @param Marca por asignar al vehículo
 */ 
    public Vehiculo(String marca){
        this.marcaVehiculo = marca;
    }

/**
 * Establece la velocidad máxima del vehículo
 * @param Velocidad por asignar
 */ 
    public void setmaxSpeed(int theSpeed){
        mymaxSpeed = theSpeed;
    }

/**
 * Invoca metodo para conocer la velocidad del vehículo
 * @return velocidad obtenida del metodo invocado
 */ 
    public int getMymaxSpeed(){
        return f();
    }
/**
 * Determina la velocidad del vehículo
 * @return velocidad del vehículo
 */ 
    public int f(){
        return mymaxSpeed;
    }
/**
 * Indica el atributo "marca" que tiene el vehículo
 * @return marca del vehículo en cuestión 
 */ 

    public String toString(){
        return marcaVehiculo;
    }

}
