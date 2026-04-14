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

        public void media()
        {
            double total = 0;
            
            for (int i = 1; i < 5; i++)
            {
                Console.WriteLine($"Insira a {i}ª nota: ");
                var numero = double.Parse(Console.ReadLine()!);
                total += numero; 
            }
            Console.WriteLine($"A media é igual a {total/4}");
        }
    }
}