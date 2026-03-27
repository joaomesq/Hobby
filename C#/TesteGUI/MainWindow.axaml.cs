using Avalonia.Controls;
using Avalonia.Interactivity;

namespace TesteGUI;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
    }

    public void Botao_Click(object sender, RoutedEventArgs e)
    {
        TextoBoasVindas.Text = "O botão foi clicado no Ubuntu!";
    }

}