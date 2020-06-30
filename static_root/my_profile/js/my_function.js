function create_news(news){
    for(var i = 0 ; i < news.length ; i++)
    {
    var div1 = document.createElement('div')
    var div3 = document.createElement('div')
    var div4 = document.createElement('div')
    var div5 = document.createElement('div')
    var div2 = document.createElement('div')
    var image = document.createElement('img')
    var aHref = document.createElement('a')
    div1.className = "col-lg-4 course_box"	
    div2.className = "card"
    div3.className = "card-body text-center"
    div4.className = "card-title"
    div5.className = "card-text"
    
        
    image.src = news[i].image
    image.className = "card-img-top"
    div2.appendChild(image)

    aHref.innerText = news[i].title
    aHref.href = "news/" + news[i].id
    div4.appendChild(aHref)
    div5.innerText = news[i].explanation
    div3.appendChild(div4)
    div3.appendChild(div5)
    div2.appendChild(div3)
    div1.appendChild(div2)
    document.getElementById('site_news').appendChild(div1)
    
    }}