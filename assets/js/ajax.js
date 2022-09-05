function like(slug, id){
    var element = document.getElementById(element = 'like')
    var count = document.getElementById(element = 'count')
    $.get(`/post/ajax/${slug}/${id}`).then(response => {
    	if(response['response'] === 'likes'){
            element.className = 'fa fa-heart'
            count.innerText = Number(count.innerText) + 1
        }else{
            element.className = 'fa fa-heart-o'
            count.innerText = Number(count.innerText) - 1
        }
    })
}
