1);
buffer.append(b ? "true" : "false");
return;
}
String s = String.valueOf(b);
print(s.toCharArray());
return;
}
if (b instanceof Character) {
    print("'");
    print(b);
    print("'");
    return;
}
print("Unexpected type;
got (" + b.getClass().getName() + ")");
}