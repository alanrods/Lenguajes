/**
 * Ejemplifica la elección de constructores
 * 
 */
public class Vehiculo {
    private static final int SPEED = 250;
    private String marcaVehiculo;
    private int mymaxSpeed = 350;

    public Vehiculo(){
        this.marcaVehiculo = "Sin Marca";
    }

    public Vehiculo(String marca){
        this.marcaVehiculo = marca;
    }

    public void setmaxSpeed(int theSpeed){
        mymaxSpeed = theSpeed;
    }

    public int getMymaxSpeed(){
        return f();
    }

    public int f(){
        return mymaxSpeed;
    }

    public String toString(){
        return marcaVehiculo;
    }

}
