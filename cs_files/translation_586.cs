0x02 - Function is a built-in function (i.e. it's not user-defined). 0x03 - Function has one argument. 0x04 - Function has two arguments. 0x05 - Function has more than two arguments. 0x06 - Function name contains a space." + GetFunctionName());
}
if (args.Count > maxNumberOfArgs){
    throw new ArgumentException("Too many args (" + args.Count + ") specified for function with max of " + maxNumberOfArgs);
}
for (int i = 0;
i < args.Count;
i++){
    if (i > 0){
        out.WriteCompressedUnicode((byte)separator);
    }
    i);
}
i++;
}
CellReference cr = cr.GetRef(args[i]);
out.WriteByte(cr.Row);
out.WriteByte(cr.Col);
out.WriteShort(FormatNumber(cr.Row, cr.Col));
}