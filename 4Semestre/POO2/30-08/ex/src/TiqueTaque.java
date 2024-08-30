public class TiqueTaque {
    String estado; // estado do rel�gio

    public synchronized void tique(boolean running) {
        if (!running) { // desliga o rel�gio
            estado = "tiqueOff";
            //notify(); // notifica a thread que est� esperando
            return;
        }
        System.out.print("Tique ");
        estado = "tiqueOff"; // define o estado atual com tiqueOff
        //notify(); // permite que taque() seja executado, tique() notifica
        // taque()

    }

    public synchronized void taque(boolean running) {
        if (!running) { // desliga o rel�gio
            estado = "taqueOff";
            notify(); // notifica a thread que est� esperando
            return;
        }
        System.out.println("Taque");
        estado = "taqueOff"; // define o estado atual com taqueOff
        notify(); // permite que tique() seja executado, taque() notifica
        // tique()
        }
}
