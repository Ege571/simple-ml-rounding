import numpy as np

W = np.random.rand()
b = np.random.rand()

learning_rate = 0.01
epoch = 2000

for _ in range(epoch):
    x_train = np.random.uniform(0, 100)
    target = round(x_train)

    tahmin = W * x_train + b
    error = tahmin - target

    b = 0
    W -= learning_rate * error
    b -= learning_rate * error
print("model hazır")

while True:
    user_input = input ("bir sayı giriniz (çıkmak için 'kapat' yazınız):")
    if user_input.lower() == "kapat":
        print("program kapandı")
        break

    try:
        x = float(user_input)
        tahmin = W * x + b
        print("Model Tahmini:", round(tahmin))

    except ValueError:
        ("geçerli bir sayı giriniz")    
    
