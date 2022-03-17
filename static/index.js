const vm = new Vue({ // Again, vm is our Vue instance's name for consistency.
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: {
        greeting: 'Hello, Vue!',
        my_message: '',
        name_val: '',
        achievement_val: '',
        sig_val:  '',
        template_val: 'Basic Template',
        img_url: "http://192.168.1.103:5000/view_image?name_val=Your Name Here&achievement_val=Achievement Description Here&sig_val=Your Signature Here&template_val=Basic Template&logo_filename_val=",
        imgUrl: '',
        image: null,
        logo_filename_val: ''
    },
    methods: {
    	async get_message() {
    		this.img_url = "http://192.168.1.103:5000/view_image?name_val="+this.name_val+"&achievement_val="+this.achievement_val+"&sig_val="+this.sig_val+"&template_val="+this.template_val+"&logo_filename_val="+this.logo_filename_val

    	},
    	onPickFile() {
    		this.$refs.fileInput.click()
    	},
    	async onFilePicked(event) {
    		const files = event.target.files
    		let filename = files[0].name
    		const fileReader = new FileReader()
    		fileReader.addEventListener('load', () => { this.imgUrl = fileReader.result })
    		fileReader.readAsDataURL(files[0])
    		this.image = files[0]
    		var d = new FormData()
    		d.append("file", this.image)
    		this.logo_filename_val = fetch("upload_file", {method: "POST", body: d}).then((result) => {return result.text()}).then((result2) => { 
    			this.logo_filename_val = result2
    			this.get_message()
    		})

    	}
    }
})