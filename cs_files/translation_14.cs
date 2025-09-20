public override bool ready(){
    lock (@lock){
        if (in == null){
            throw new System.IO.IOException("InputStreamReader is closed");
        }
        try{
            return bytes.Remaining() > 0 || @in.Available() > 0;
        }
        catch (System.IO.IOException){
            return false;
        }
    }