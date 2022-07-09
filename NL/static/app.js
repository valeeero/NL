new Vue({
    el: '#notes_app',
    data: {
    notes: []
    },
    created: function () {
        const vm = this;
        axios.get('/api/note_lists/')
        .then( function (response){
        vm.notes = response.data
        })
    }
}

)