import java.util.Stack;
import java.util.Queue;
import java.util.*;

public class simonguzman {
    public static void main(String[] args) {
        //Pilas
        Stack<String> books = new Stack<>();
        //Agregando elementos a la piila
        books.push("Cien años de soledad");
        books.push("El amor en los tiempos del colera");
        books.push("El pianista del gueto de varsovia");
        //Monstrando la pila
        System.out.println(books);
        //Mostrar el ultimo elemento de la pila, el ultimo que entro en esta
        System.out.println("Ultimo elemento de la pila: "+ books.peek());
        //Eliminar el ultimo elemento de la pila, el ultimo que entro
        books.pop();
        //Mostrar la pila actualizada
        System.out.println(books);
        //Buscar la posicion del elemento en la pila
        System.out.println("Posicion del libro: "+books.search("Cien años de soledad"));

        //Colas
        Queue<String> cola = new LinkedList<>();
        //Añadir elementos a la cola
        cola.add("Simon");
        cola.add("Julian");
        cola.add("Camilo");
        //Mostrar la cola
        System.out.println(cola);
        //Remover elemento
        cola.remove();
        System.out.println(cola);
        //Alternativa a remover elemento
        cola.poll();
        System.out.println(cola);
        //Consultar el primer elemento de la cola
        System.out.println(cola.element());
        System.out.println(cola.peek());
        //Tamaño de la cola
        System.out.println(cola.size());

        navegadorWeb();
    }

    public static void navegadorWeb(){
        Stack<String> historial = new Stack<>();
        Scanner sc = new Scanner(System.in);
        int index = -1;
        String opcion;
        do{
            System.out.println("Ingrese pagina, adelante, atras, o salir: ");
            opcion = sc.next();
            if(opcion.equals("pagina")){
                index = ingresarPagina(historial);
            }else{
                index = opcionesNavegador(historial, opcion, index);
            }
        }while(!opcion.equals("salir"));
        
    }

    public static int opcionesNavegador(Stack<String> pila, String opcion, int index){
        switch (opcion) {
            case "adelante":
            index = accionAdelante(pila, index);
                break;
            case "atras":
            index = accionDetras(pila, index);
            break;
            case "salir":
            System.out.println("Saliendo del programa.....");
            break;
            default:
            System.out.println("Opcion no valida");
                break;
        }
        return index;
    }

    public static int ingresarPagina(Stack<String> pila){
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese la url de la pagina: ");
        String pagina = sc.next();
        pila.push(pagina);
        System.out.println("Has navegado a: "+pagina);
        return pila.size()-1;
    }

    public static int accionAdelante(Stack<String> pila, int index){
        if(validarPilaVacia(pila)){
            if(index < pila.size() - 1){
                index++;
                System.out.println("Link de pagina: "+pila.get(index));
            }else{
                System.out.println("No hay mas historial hacia adelante\n");
                //index = pila.size() - 1;
            }
        }else{
            System.out.println("No hay historial");
        }
        return index;
    }

    public static int accionDetras(Stack<String> pila, int index){
        if(validarPilaVacia(pila)){
            if(index > 0){
                index--;
                System.out.println("Link de pagina: "+pila.get(index));
            }else{
                System.out.println("No hay mas historial hacia adelante\n");
            }
        }else{
            System.out.println("No hay ningun historial");
        }
        return index;
    }

    public static boolean validarColaVacia(Queue<String> cola){
        return !cola.isEmpty();
    }

    public static boolean validarPilaVacia(Stack<String> pila){
        return !pila.isEmpty();
    }

}
