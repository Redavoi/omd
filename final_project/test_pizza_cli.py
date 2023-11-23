from unittest.mock import patch
from click.testing import CliRunner
from pizza_cli import cli


def test_order_pizza_with_delivery():
    """
    Тестирует заказ пиццы с доставкой. Проверяет код выхода,
    вывод и вызовы моков.
    """
    runner = CliRunner()

    with patch('pizza_services.create_pizza') as mock_create, \
         patch('pizza_services.delivery') as mock_delivery, \
         patch('pizza_services.pickup') as mock_pickup:

        result = runner.invoke(cli, ['order', 'Margherita', 'L', '--delivery'])
        assert result.exit_code == 0
        assert "You ordered a" in result.output
        mock_create.assert_called_once_with(name='Margherita', size='L')
        mock_delivery.assert_called_once()
        mock_pickup.assert_not_called()


def test_order_pizza_pickup():
    """
    Тестирует заказ пиццы с самовывозом. Проверяет код выхода и вывод.
    """
    runner = CliRunner()

    with patch('pizza_services.create_pizza') as mock_create, \
        patch('pizza_services.pickup') as mock_pickup:

        result = runner.invoke(cli, ['order', 'Pepperoni', 'XL'])
        assert result.exit_code == 0
        assert "You ordered a" in result.output
        mock_create.assert_called_once_with(name='Pepperoni', size='XL')
        mock_pickup.assert_called_once()


def test_menu():
    """
    Тестирует отображение меню. Проверяет код выхода и содержание вывода.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ['menu'])
    assert result.exit_code == 0
    assert "Menu:" in result.output
    assert "Margherita" in result.output
    assert "Pepperoni" in result.output
    assert "Hawaiian" in result.output


def test_order_pizza_with_invalid_option():
    """
    Тестирует заказ пиццы с невалидной опцией. Проверяет код выхода и
    сообщение об ошибке.
    """
    runner = CliRunner()

    result = runner.invoke(cli, ['order',
                                 'Margherita',
                                 'Medium',
                                 '--delivery'])

    assert result.exit_code == 2
    assert "'Medium' is not one of" in result.output
