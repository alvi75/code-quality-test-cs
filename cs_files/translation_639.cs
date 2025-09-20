public override long ValueFor(int elapsed){
    double val;
    switch (Type){
        case Type.OneShapedouble d0 = elapsed - Offset0;
        if(d0 < 0 || d0 > 1){
            val = 0;
        }
        else if (d0 == 1){
            val = Multiplier;
        }
        else{
            val = (elapsed - Offset1) * Multiplier;
        }
        if (Mode == 0){
            return (long)Math.Round(val);
        }
        else{
            return (long)(val + 0.5D) + 1L;
        }
    }