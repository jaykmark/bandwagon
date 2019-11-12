const onSuccessArtist = (res) =>{
    console.log(res)
    $('.card').remove()
    artists = JSON.parse(res.artists)
    artists.forEach(artist => {
        $('#artist-list').append(artistTemplate(artist))
    })
}
const onSuccessBand = (res) => {
    bands = JSON.parse(res.bands)
    $('.card').remove()
    bands.forEach(band => {
        $('#band-list').append(bandTemplate(band))
    })
}
const onErr = (err) => {
    console.log(err)
}

const bandTemplate = (band) => {
    
    return `  <div class="card">
    <div class="card-background">
      <div class="card-image">
        <img src=${band.fields.image_link} alt=${band.fields.name}/>
      </div>

      <div class="card-name">${band.fields.name}</div>
      <div class="card-description">${band.fields.description}</div>
      <a href=./${band.pk}>MORE</a>
    </div>
  </div>
`
}

const artistTemplate = artist =>{
    return `<div class="card">  
    <div class="card-background">
    <div class="card-image">
    <img src="${artist.fields.image_link}" alt="${artist.fields.stage_name}"/>
    </div>

    <div class="card-name">${artist.fields.stage_name}</div>
    <div class="card-description">${artist.fields.description}</div>
    <a href="./${artist.pk}" class="card-button btn">MORE</a>
</div>
</div>`
}
$('#artist-search').on('keyup',function(event){
    event.preventDefault()
    let query = {query:$('#artist-query').val()}
    $.ajax({
        method:'GET',
        url:'./search',
        data:query,
        success:onSuccessArtist,
        error:onErr
    })
})
$('#band-search').on('keyup',function(event){
    event.preventDefault()
    let query = {query:$('#band-query').val()}
    $.ajax({
        method:'GET',
        url:'./search',
        data:query,
        success:onSuccessBand,
        error:onErr
    })
})