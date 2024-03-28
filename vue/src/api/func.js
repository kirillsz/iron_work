
function getBase64(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = error => reject(error);
    });
}

function convert_image(name, size, format) {

    if(name === null) return

    let reg_str = "upload/c_scale,w_" + size + "/"
    let img = name.replace(/upload\//g, reg_str)

    let res = img.split(".")
    res = res.slice(0, res.length-1)
    res.push(format)

    return res.join(".")
}

function trun(s, l) {
    if(s === undefined) return "";
    return s.length > l ? s.substring(0, l) + "..." : s.substring(0, l);
}



export { convert_image, trun, getBase64 }