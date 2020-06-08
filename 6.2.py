from fractions import Fraction as frac
from collections import defaultdict

#1-st task 
class Array:
    def __init__(self, size=0, elements=[]):
        self.size = size
        if size and not elements:
            self.elements = [None] * size
        elif elements:
            self.elements = sorted(elements)
        else:
            self.elements = []

    def getindex(self, item):
        index = self.binarySearch(item)
        return index

    def binarySearch(self, target):
        start, end = 0, self.size
        while not (end - start < 0):
            mid = ((end - start) // 2) + start
            if self.elements[mid] == target:
                return mid
            elif self.elements[mid] < target:
                start = mid + 1
            elif self.elements[mid] > target:
                end = mid - 1
        return -1

    def insert(self, element):
        self.elements.append(element)
        self.size += 1
        self.elements.sort()

    def pop(self, index=-1):
        self.elements.pop(index)
        self.size -= 1

    def __getitem__(self, index):
        return self.elements[index]

    def __del__(self):
        self.elements = None

    def sort(self):
        self.mergeSort(self.elements)

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2  # Finding the mid of the array
            L = arr[:mid]  # Dividing the array elements
            R = arr[mid:]  # into 2 halves

            mergeSort(L)  # Sorting the first half
            mergeSort(R)  # Sorting the second half
            i = j = k = 0
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    def test(self):
        shorts = [-32768, 32767, 755, 43, 5, 2, 6, 8, 4, 3]
        ints = [-2147483648, 2147483647, 32767, 755, 43, 5, 0, 6, 8, 4, 3]
        longs = [-9223372036854775808, 9223372036854775807,
                 32767, 755, 43, 5, 2, 6, 0, 4, 3]
        strings = ["5", "10", "9", "101"]
        fracts = [frac('-12.23'), frac('123.03'), frac('-12343212.11')]
        self.test_data(shorts)
        self.test_data(ints)
        self.test_data(longs)
        self.test_data(strings)
        sort_test = Array(len(strings), strings)
        self.test_data(fracts)

    def test_data(self, data):
        data_array0 = Array()
        for elem in data:
            data_array0.insert(elem)
        self.self_check(data, data_array0)
        data_array1 = Array(len(data), data)
        self.self_check(data, data_array1)
        del self

    def self_check(self, insert_elements, array):
        for idx in range(len(insert_elements)):
            index = array.getindex(array[idx])
            print("%d == %d" % (idx, index), idx == index)
            print("Index of the element %s is %d" % (str(array[idx]), index))


class Menu:
    def __init__(self, blyuda=[]):
        self.blyuda = blyuda

    def add(self, blyudo):
        self.blyuda.append(blyudo)

    def __del__(self):
        self.blyuda = []


class Eda:
    def __init__(self, name="", price=0, producty=[]):
        self.producty = producty
        self.price = price
        self.name = name

    def get_price(self):
        return self.price

    def add(self, product):
        self.blyuda.append(product)

    def __del__(self):
        self.producty = []


class Product:
    def __init__(self, name="", price=0):
        self.price = price
        self.name = name

    def get_price(self):
        return self.price

    def prepare(self):
        print(self.name + "був приготований до вживання")


class Client:
    def __init__(self, name):
        self.name = name


class Zakaz:
    def __init__(self, client, producty=[], blyuda=[]):
        self.producty = producty
        self.blyuda = blyuda
        self.client = client
        self.chay = 0

    def dobavit_v_zakaz(self, item):
        if isinstance(item, Product):
            self.producty.append(item)
        elif isinstance(item, Eda):
            self.blyuda.append(item)

    def dobavit_chaeviye(self, chay):
        self.chay = chay

    def summa_zakaza(self):
        summa_blyud = sum([x.get_price() for x in self.blyuda])
        summa_productov = sum([x.get_price() for x in self.producty])
        return summa_blyud + summa_productov + self.chay

    def __del__(self):
        self.producty = []
        self.blyuda = []


class Den_s_Zakazami:
    def __init__(self, zakazi=[]):
        self.zakazi = zakazi
        self.total = 0

    def summa_za_den(self):
        self.total = sum([x.summa_zakaza() for x in self.zakazi])
        print("Za etot den summa = ", self.total)

    def infa_pro_vse_blyuda(self):
        vse_blyuda = defaultdict(dict)
        vse_producty = defaultdict(dict)
        for zakaz in self.zakazi:
            for blyudo in zakaz.blyuda:
                if blyudo not in vse_blyuda:
                    vse_blyuda[blyudo] = {
                        "viruchka": blyudo.get_price(), "skolko_zakazali": 1}
                else:
                    vse_blyuda[blyudo]["viruchka"] += blyudo.get_price()
                    vse_blyuda[blyudo]["skolko_zakazali"] += 1

            for product in zakaz.producty:
                if product not in vse_producty:
                    vse_producty[product] = {
                        "viruchka": product.get_price(), "skolko_zakazali": 1}
                else:
                    vse_producty[product]["viruchka"] += product.get_price()
                    vse_producty[product]["skolko_zakazali"] += 1

    def __del__(self):
        self.zakazi = []


if __name__ == "__main__":
    array = Array()
    array.test()

