namespace Exercicios
{
    public class Exercicio1
    {
        public void tabuada(int numero = 1)
        {
            for (int i = 1; i < 11; i++)
            {
                var valor = numero * i;
                Console.WriteLine($"{numero} * {i} = {valor}");
            }
        }

        public double media(params double[] numeros)
        {
            double total = 0;
            foreach (double numero in numeros)
            {
                total += numero;
            }
            return total/numeros.Length;
        }
    }
}