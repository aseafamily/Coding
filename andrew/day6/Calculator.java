class  Calculator {
    public static void main(String[] args) {
        System.out.println("I am a calculator! Please type a mumber:");

        double x = Double.parseDouble(System.console().readLine());

        System.out.println("Please type a operation (+-*/)");
        String o = System.console().readLine();

        System.out.println("Please type another mumber:");

        double y = Double.parseDouble(System.console().readLine());
        double z = 0;

        if (o.equals("+")) {
            z = x + y;
        }
        if (o.equals("-")) {
            z = x - y;
        }
        if (o.equals("*")) {
            z = x * y;
        }
        if (o.equals("/")) {
            z = x / y;
        }
        System.out.println("I knew the answer of " + x + o + y + " = " +z);
    }
}
