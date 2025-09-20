1 : n = 0;
data = new char[bufferSize];
}
else if (n == data.length) {
    char[] newData = new char[n + blockSize];
    System.arraycopy(data, 0, newData, 0, n);
    data = newData;
}
}