from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def my_shop():
    return render_template('basestemp.html')

@app.route('/clothes/')
def clothes():
    clothes = {
        'name': 'Наименование товара',
        'size': 'Размеры в наличии',
        'amount': 'Количество'
    }

    clothes_list = [
        {
            'name': 'Рубашка',
            'size': 'XS, S, M, L, XL, XXL',
            'amount': 10
        },
        {
            'name': 'Юбка',
            'size': 'S, M, L, XXL',
            'amount': 5
        },
        {
            'name': 'Брюки',
            'size': 'XS, S, L, XXXL',
            'amount': 12
        }
    ]
    return render_template('index_clothes.html', **clothes, clothes_list=clothes_list)

@app.route('/shoes/')
def shoes():
    shoes = {
        'name': 'Наименование товара',
        'size': 'Размер',
        'amount': 'Количество'
    }

    shoes_list = [
        {
            'name': 'Кроссовки для бега',
            'size': '20-36',
            'amount': 6
        },
        {
            'name': 'Ботинки',
            'size': '36-44',
            'amount': 7
        }
    ]
    return render_template('index_shoes.html', **shoes, shoes_list=shoes_list)
    # return render_template('index_shoes.html')
#
@app.route('/accessories/')
def accessories():
    accessories ={
        'name': 'Наименование товара',
        'size': 'Размер',
        'amount': 'Количество'
    }
    accessories_list = [
    {
        'name': 'Шапка',
        'size': '54-56',
        'amount': 8
    },
    {
        'name': 'Перчатки',
        'size': '5-8',
        'amount': 10
    }
    ]


    return render_template('index_accessories.html', **accessories, accessories_list=accessories_list)

if __name__ == '__main__':
    app.run(debug=True)