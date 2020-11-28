from src import ejemplo2



def test_init_data_None():
    dataset = ejemplo2.Dataset()
    assert None == dataset.data


def test_load_data_del_dataset(mocker):
    def mock_load(self):
        # agregar logica diferente del metodo original.
        # Agregar logica a testear.
        self.data = 'hola'
        return 1

    mocker.patch(
        'src.ejemplo2.Dataset.load_data',
        mock_load
    )

    dataset = ejemplo2.Dataset()
    assert 1 == dataset.load_data()
    assert 'hola' == dataset.data

