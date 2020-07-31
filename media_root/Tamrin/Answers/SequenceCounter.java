public class SequenceCounter {
    private int time;
    private int[] timeOutput;
    public SequenceCounter(){
        time=0;
        timeOutput=new int[4];
    }
    public void INR(){
        if (time<3){
            time++;
        }
    }
    public void CLR(){
        time=0;
    }
    public void timeDecoder(){
        clear();
        timeOutput[time]=1;
    }
    public void clear(){
        for (int out:timeOutput)
            out=0;
    }

}
