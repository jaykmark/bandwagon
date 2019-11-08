const onSuccess = (res) =>{
    console.log(res)
    artists = JSON.parse(res.artists)
    artists.forEach(artist => {
        console.log(artist.fields.stage_name)
    })
}
const onErr = (err) => {
    console.log(err)
}

$('#search').on('submit',function(event){
    event.preventDefault()
    let query = {query:$('#query').val()}
    $.ajax({
        method:'GET',
        url:'./artists/search',
        data:query,
        success:onSuccess,
        error:onErr
    })
})