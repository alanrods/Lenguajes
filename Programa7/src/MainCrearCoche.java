/**
 * Created by ivanf on 05/05/2016.
 */
public class MainCrearCoche {
    public static void main(String[] args) {

    /*Se manda a llamar diferentes instancias de la clase coche para demostrar el encademiento de constructores*/

        Coche Coche_sin_marca = new Coche();    //Constructor default
        Coche BMW = new Coche("BMW"); //Creando un BMW  //Constructor con solo marca
        Coche BMW_placas = new Coche("BMW", 12345); //Constructor con marca y placas
        Coche BMW_placas_y_color = new Coche("BMW", 6789, "Negro"); // Constructor con marca, placas y color
        Moto motocicleta = new Moto();

        System.out.println(Coche_sin_marca);
        System.out.println(BMW);
        System.out.println(BMW_placas);
        System.out.println(BMW_placas_y_color);
        //Si se intenta acceder a ese parametro el compilador nos dria que es privado
        //System.out.println(BMW.marcaCoche);
        //Nuevamente, se nos negara la modificacion del atributo de privado de una clase
        // A menos de que estemos dentro de ella.
        //BMW.mymaxSpeed = 400;

        //Se utiliza un getter para poder modificar los valores y getter para poder observarlos.
        System.out.println("\nCambiando variables de tipo privado con un setter");
        BMW.setmaxSpeed(400);

        System.out.println("\nMostrando la busqueda dinamica de metodos");
        /*Las clases siempre buscan en si mismas por un metodo y despues en las demas de las que heredan
        dependiendo de su orden, en este caso la clase BMW no tiene metodo f() por lo que lo busca en la clase padre
        y lo encuentra mientras que la clase motocicleta cuenta con el metodo f() por lo cual regresa el valor que
        especifica su funcion*/
        System.out.println(BMW.getMymaxSpeed());
        System.out.println(motocicleta.getMymaxSpeed());

    }
}
