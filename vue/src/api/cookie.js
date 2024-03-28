

export function set_cookie(key, value, expire){

    const date = new Date(expire);
    document.cookie = key + "=" + value + "; expires=" + date + "; path=/; SameSite=Lax";
}

export function get_cookie(n) {
    let a = `; ${document.cookie}`.match(`;\\s*${n}=([^;]+)`);
    return a ? a[1] : '';
}
