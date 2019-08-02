var dataList = document.getElementById('json-datalist')

data.forEach(movie => {
    var option = document.createElement('option')
    option.value = movie['Title']
    dataList.appendChild(option)
})
