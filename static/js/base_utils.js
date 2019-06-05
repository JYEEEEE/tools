function ajaxGet(url, data, callback) {
    $.ajax({
        url: url,
        dataType: "JSON",
        type: "GET",
        success: function (result) {
            if (isNotEmpty(callback)) {
                callback(result);
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            if (403 !== XMLHttpRequest.status) {
                alert("错误:" + XMLHttpRequest.responseText);
            } else {
                try {
                    eval(XMLHttpRequest.responseText);
                } catch (e) {
                    alert("错误:" + XMLHttpRequest.responseText);
                }
            }
        }
    });
}


function ajaxPost(url, data, callback) {
    set_xsrf(data);
    $.ajax({
        url: url,
        data: data,
        dataType: "JSON",
        type: "POST",
        success: function (result, textStatus) {
            if (textStatus === "success") {
                if (callback) {
                    callback(result);
                }
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            ("错误：服务器异常，请重试！");
        },
        complete: function (XMLHttpRequest, textStatus) {
            // TODO 页面遮罩去除等等
        }
    });
}


function syncAjaxPost(url, data, callback) {
    set_xsrf(data);
    $.ajax({
        url: url,
        data: data,
        dataType: "JSON",
        type: "POST",
        async: false,
        success: function (result, textStatus) {
            if (textStatus === "success") {
                if (callback) {
                    callback(result);
                }
            }
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            alert("错误：服务器异常，请重试！");
        },
        complete: function (XMLHttpRequest, textStatus) {
            // TODO 页面遮罩去除等等
        }
    });
}


function set_xsrf(data) {
    var secure_key = $.cookie("_xsrf");
    if (secure_key) {
        data["_xsrf"] = secure_key;
    }
    data["v"] = new Date().getTime();
    return data;
}

function confirm_dialog(title, content, ok_callback, cancel_callback) {
    layer.confirm(content,
        {
            icon: 3,
            btn: ["确认", "取消"],// 按钮
            title: title || '提示'
        },
        function (index) {
            if (ok_callback) {
                ok_callback && ok_callback();
            }
            layer.close(index);
        },
        function (index) {
            if (cancel_callback) {
                cancel_callback && cancel_callback();
            }
            remove_loading();
            layer.close(index);
        }
    );
}

function iframe_dialog(title, url, width, height, ok_callback) {
    layer.open({
        type: 2,
        title: title || "提示",
        area: [width || '500px', height || '200px'],
        content: url, //iframe的url，出现滚动
        yes: function (index) {
            if (ok_callback) {
                ok_callback && ok_callback();
            }
            layer.close(index);
        },
        cancel: function (index) {
            remove_loading();
            layer.close(index);
        }
    });
}

function custom_dialog(url, width, height) {
    if (url.indexOf("?") !== -1) {
        url = url + '&v=' + (new Date()).valueOf();
    } else {
        url = url + '?v=' + (new Date()).valueOf();
    }
    $.ajax({
        url: url,
        type: "GET",
        async: false,
        success: function (result) {
            pop = layer.open({
                type: 1,
                title: false,
                resize: false,
                // scrollbar: false,
                shade: 0.6,
                shadeClose: true, //开启遮罩关闭
                area: [width || '500px', height || '200px'],
                content: result //iframe的url，出现滚动
            });
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            if (403 !== XMLHttpRequest.status) {
                alert("错误:" + XMLHttpRequest.responseText);
            } else {
                try {
                    eval(XMLHttpRequest.responseText);
                } catch (e) {
                    alert("错误:" + XMLHttpRequest.responseText);
                }
            }
        }
    });
    return pop;
}

function frame_pop(title, url, width, height, ok_callback, end_callback) {
    layer.open({
        type: 2,
        title: title || "提示",
        area: [width || '500px', height || '200px'],
        btn: ["确认", "取消"],// 按钮
        content: url, //iframe的url，出现滚动
        yes: function () {
            if (ok_callback) {
                ok_callback && ok_callback();
            }
        },
        cancel: function (index) {
            remove_loading();
            layer.close(index);
        },
        end: function () {
            if (end_callback) {
                end_callback && end_callback();
            }
        }
    });
}

function message_dialog(title, content, callback) {
    layer.alert(content, {
            icon: 3,
            btn: ["确认"], // 按钮
            title: title || '提示'
        },
        function (index) {
            if (callback) {
                callback && callback();
            }
            layer.close(index);
        }
    );
}

function tip_msg(content, timeout, callback) {
    layer.msg(content, {
        shade: 0.2,
        time: timeout || 2000,
        end: function () {
            if (callback) {
                callback && callback();
            }
        }
    })
}

function success_msg(content, timeout, callback) {
    var index = layer.msg(content, {
        icon: 1,
        shade: 0.2,
        time: timeout || 2000,
        end: function () {
            if (callback) {
                callback && callback();
            }
        }
    });
    layer.style(index, {
        borderRadius: '5px'
    });
}

function fail_msg(content, timeout, callback) {
    var index = layer.msg(content, {
        icon: 2,
        shade: 0.2,
        time: timeout || 2000,
        end: function () {
            if (callback) {
                callback && callback();
            }
        }
    });
    layer.style(index, {
        borderRadius: '5px'
    });
}

function entry_dialog(title, width, height, content, suc_callback, yes_callback, end_callback) {
    layer.open({
        type: 1,
        title: title,
        area: [width, height],
        btn: ["确认", "取消"],
        content: content,
        success: function () {
            if (suc_callback) {
                suc_callback && suc_callback();
            }
        },
        yes: function () {
            if (yes_callback) {
                yes_callback && yes_callback();
            }
        },
        end: function () {
            if (end_callback) {
                end_callback && end_callback();
            }
        }
    });
}

var loading = null;

function display_loading() {
    loading = layer.load(2, {
        shade: 0.1
    });

}

function remove_loading() {
    if (loading) {
        layer.close(loading)
    }
}


function dict_2_url_params(dict) {
    var result = '';
    try {
        if (dict) {
            for (var key in dict) {
                result += key + '=' + dict[key] + "&";
            }
        }
    } catch (error) {

    }
    if (result.length > 0) {
        result = result.slice(0, result.length - 1)
    }
    return result;
}

function get_attribute_list(category, parent_code) {
    var attribute_list = null;
    if (category) {
        var data = {"category": category, 'parent_code': parent_code};
        syncAjaxPost("/common/attribute/", data, function (result) {
            if (result.code === 1) {
                attribute_list = result.attribute_list;
            } else if (result.code === -1) {
                tip_msg("请指定一个查询类别！", 2000);
            } else {
                tip_msg("抱歉，暂时无法获取数据！", 2000);
            }
            remove_loading()
        });
    } else {
        tip_msg("请指定一个查询类别！", 2000);
    }
    return attribute_list;
}


//模仿python的使用习惯, 0|[]|{}|""这些都返回false
function empty(obj) {
    if (typeof (obj) === "undefined" || null === obj) {
        return true;
    }
    if (typeof (obj) === "function") {
        return false;
    }
    if (obj.constructor === Number) {
        return !(obj || 0 === obj);
    } else if (typeof (obj) === "string") {
        return obj === "";
    } else {
        if (obj.hasOwnProperty('length') && obj.length === 0) {
            return true;
        }
        for (var prop in obj) {
            if (obj.hasOwnProperty(prop)) {
                return false;
            }
        }
        return true;
    }
}

function isNotEmpty(obj) {
    return !empty(obj);
}

//strip函数
String.prototype.strip = function () {
    return this.replace(/^\s*(.*?)\s*$/, "$1");
};


function dialog(title, url, width, height, ok_callback, show_callback) {
    $.ajax({
        url: url,
        type: "GET",
        async: false,
        success: function (result) {
            pop = layer.open({
                type: 1,
                title: title || "提示",
                area: [width || '500px', height || '200px'],
                content: result, //iframe的url，出现滚动
                yes: function (index) {
                    if (ok_callback) {
                        ok_callback && ok_callback();
                    }
                    layer.close(index);
                },
                cancel: function (index) {
                    remove_loading();
                    layer.close(index);
                },
                success: function () {
                    show_callback && show_callback();
                }
            });
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            if (403 !== XMLHttpRequest.status) {
                alert("错误:" + XMLHttpRequest.responseText);
            } else {
                try {
                    eval(XMLHttpRequest.responseText);
                } catch (e) {
                    alert("错误:" + XMLHttpRequest.responseText);
                }
            }
        }
    });
    return pop;
}
