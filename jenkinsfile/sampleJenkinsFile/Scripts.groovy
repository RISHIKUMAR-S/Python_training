def Build_App(){
    echo 'Building the app'
}

def Test_App(){
    echo "Testing the app version ${params.VERSION}"
}

def Deploy_App(){
    echo "deploying the app version ${params.VERSION}"
}
// return this

return [
    Build_App: this.&Build_App,
    Test_App: this.&Test_App,
    Deploy_App: this.&Deploy_App
]