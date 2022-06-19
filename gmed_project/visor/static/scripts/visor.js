
$(function () {
    let pairs_dots = []
    const dotPairs = [
        ["S", "N"],
        ["N", "A"],
        ["N", "B"],
        ["S", "Go"],
        ["N", "Me"],
        ["Go", "Me"],
        ["SNP pm", "SNA"],
        ["N", "Se"],
        ["Go", "Ar"],
        ["Go", "N"],
        ["Po", "Or"],
        ["S", "Ar"],
        ["N", "Pog"],
        ["ii", "is"],
//                ["P6", "I"],
        ["ais", "is"],
        ["aii", "ii"],
        ["EN pn", "DT pog"],
        ["A", "B"],
        ["EN pn", "Sn"],
        ["Sn", "UL"],
        ["Sn", "DT pog"],
        ["S", "Gn"],
//                ["B", "C1"],
//                ["A", "A3"],
        ["Ba", "N"]
    ]

    let zoomImage = 1
    let baseZoom = 1
    let dotList = {}
    let lastScrollTop = 1

    $('#upload_button, .no_image').on('click', uploadImage);

    function clone(obj) {
        if (null == obj || "object" != typeof obj) return obj;
        let copy = obj.constructor();
        for (let attr in obj) {
            if (obj.hasOwnProperty(attr)) copy[attr] = obj[attr];
        }
        return copy;
    }

    function getDotByName(dot_name, dot_list) {
        let res = {}
        if (dot_list[dot_name])
            res[dot_name] = clone(dot_list[dot_name])
        else
            console.log('Dot with name ' + dot_name + ' not found')
        return res
    }

    function drawLines(dot_pairs_list, dot_list) {
        for (let i = 0; i < dot_pairs_list.length; i++) {
            drawLineByDots(
                getDotByName(dot_pairs_list[i][0], dot_list)[dot_pairs_list[i][0]],
                getDotByName(dot_pairs_list[i][1], dot_list)[dot_pairs_list[i][1]]
            )
        }
    }

    function drawLineByDots(dot1, dot2) {
        $('#image_container').line(
            dot1['x'],
            dot1['y'],
            dot2['x'],
            dot2['y'])
    }

    function uploadImage() {
        $('#upload').trigger('click');

        function readURL(input) {
            if (input.files && input.files[0]) {
                let reader = new FileReader();

                reader.onload = function (e) {
                    $('.no_image').hide()
                    $('.image_wrapper').css('display', 'block')

                    $('#image_visor')
                        .attr('src', e.target.result)
                        .css('display', 'block')
                        .one("load", function () {

                            let max_side = $(this).height() > $(this).width() ?
                                $(this).height() :
                                $(this).width()

                            baseZoom = zoomImage = Math.floor($('.image_wrapper').width() * 100 / max_side) / 100

                            $('#image_container').css('zoom', zoomImage)
                        });

                    $('#recognize').removeClass('disable')
                }

                reader.readAsDataURL(input.files[0]);
            }
        }

        $("#upload").on('change', function () {
            cleanAll();
            readURL(this);
        })
    }

    $("#image_container").on("mousedown", function (ev) {
        let zoom = $('#image_container').css('zoom')
        let mouseX = (ev.pageX - ($('.content').width() - $('.visor').width()) / 2 - $('.dotList').width() - parseFloat($('.content').css('margin-top')))/zoom;
        let mouseY = (ev.pageY - $('header').height() - parseFloat($('.content').css('margin-top')))/zoom;

        $('.dot.selected')
            .not( ".ui-draggable-dragging" )
            .css('top', mouseY + 'px')
            .css('left', mouseX + 'px')
            .map(function(){
                dotList[this.title]['x'] = mouseX
                dotList[this.title]['y'] = mouseY
            })
        $("#image_container .line").remove()
        drawLines(pairs_dots, dotList)
    })

    function cleanAll() {
        $('.line').remove()
        $('.dot').remove()

    }

    function drawDot(name, y, x) {
        $("#image_container").append(
            $('<div/>')
                .addClass('dot')
                .css('top', y + 'px')
                .css('left', x + 'px')
                .css('font-size', 16 / zoomImage)
                .prop('title', name)
                .text(name)
                .draggable({
                    cursor: "crosshair",
                    disabled: true
                })
                .on("dragstop", function () {
                    dotList[$(this).attr('title')]['x'] = parseFloat($(this).css('left'))
                    dotList[$(this).attr('title')]['y'] = parseFloat($(this).css('top'))
                    $("#image_container .line").remove()

                    drawLines(pairs_dots, dotList)

                })
                .css("position", "absolute")
        );

    }

    function showDotList(container, list) {
        $(container).append(
            $('<div title="Скрыть/Показать все точки"/>')
                .append($('<input type="checkbox" checked/>').on('click', function () {
                    if ($(this).is(':checked')) {
                        $(".dot").show();
                        $(container + " input").prop('checked', true);
                    } else {
                        $(".dot").hide();
                        $(container + " input").prop('checked', false);
                    }
                }))
                .append($('<div class="all_dots">Все</div>'))
            )

        for (let key in list) {
            if (list[key]['editable'])
                $(container).append(
                    $('<div title="' + list[key]['description'] + '"/>')
                        .append($('<input type="checkbox" checked dot="' + key + '"/>').on('click', function () {
                            if ($(this).is(':checked')) {
                                $(".dot[title='" + $(this).attr('dot') + "']").show();
                            } else {
                                $(".dot[title='" + $(this).attr('dot') + "']").hide();
                            }
                        }))
                        .append($('<div class="btn">' + key + '</div>')
                            .on('click', function () {
                                $(this).toggleClass("selected");
                                $(".dot[title='" + key + "']")
                                    .toggleClass("selected")
                                    .draggable({
                                        disabled: false
                                    })
                            })
                        )
                )
        }
    }

    function setDots(list) {
        for (let key in list) {
            drawDot(key, list[key]['y'], list[key]['x'])
        }
    }

    $('#lines_hider').on('click', function () {
        $('.visor .line').toggle()
    })

    $('#recognize').on('click', function () {
        $('.overlay_popup').show()
        let filesSelected = document.getElementById("upload").files;
        if (filesSelected.length > 0) {
            let fileToLoad = filesSelected[0];
            let fileReader = new FileReader();
            fileReader.onload = function (fileLoadedEvent) {
                let srcData = fileLoadedEvent.target.result.split(';base64,')[1];
                const data = {
                    "image": srcData,
                    "filename": $('#upload').val().split('\\').pop()
                };

                fetch('/predict/',
                    {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(data),
                    }
                )
                    .then(response => response.json())
                    .then(data => {
                        dotList = Object.assign({},data.dots)
                        pairs_dots = JSON.parse(JSON.stringify(typeof data.pairs !== 'undefined' ? data.pairs : dotPairs));

                        setDots(dotList)

                        drawLines(pairs_dots, dotList)

                        if ($('.dotList').is(':empty')) {
                            showDotList('.dotList', dotList)
                        }

                        $('#decryption').removeClass('disable')
                        $('#report').removeClass('disable')
                        $('#hand_move').removeClass('disable')
                        $('#lines_hider').removeClass('disable')
                        $('#calc').removeClass('disable')
                        $('#save_btn').removeClass('disable')
                        $('.overlay_popup').hide()
                    })
                    .catch((error) => {
                        console.error('Error:', error);
                        $('.overlay_popup').hide()
                    });

            }
            fileReader.readAsDataURL(fileToLoad);
        }

    })

    $('#report').on('click', function () {
        window.open("{% static 'files/medicinskaya karta v10 (polnaia)_1649867809.pdf' %}");
    })

    $('#decryption').on("click", function () {
        let popup_id = $('#' + $(this).attr("rel"));
        $(popup_id).show();
        $('.overlay_popup, .popup').show();
    })

    $('.overlay_popup').on("click", function () {
        $('.overlay_popup, .popup').hide();
    })

    $('.image_wrapper').on('mousewheel', function (e) {
        let st = $(this).scrollTop();
        if (e.originalEvent.wheelDelta / 120 > 0) {
            zoomImage += 0.1
        } else {
            zoomImage -= 0.1
        }
        $('#image_container').css('zoom', zoomImage)
        lastScrollTop = st;

        if (zoomImage > baseZoom) {
            $('.image_wrapper').css('overflow', 'scroll')
        } else {
            $('.image_wrapper').css('overflow', 'hidden')
        }
    })

    $('#calc').on('click', function () {
        $('.overlay_popup').show()
        $.ajax({
            url: 'calculate/',
            method: 'post',
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(dotList),
            traditional: true,
            dataType: 'json'
        })
        .done(function(data) {
            console.log(data)
            $('.content').append(
                $('<div class="popup" style="display:block; position: absolute; top: 5vh; left: 5vh">'
                + '<table><tbody id="report">'
                + '<tr><td>name</td>'
                + '<td>diagnoses</td>'
                + '<td>measure</td>'
                + '<td>normal_value</td>'
                + '<td>delta</td>'
                + '<td>value</td>'
                + '<td>description</td></tr>'
                + '</tbody></table>'
                + '</div>')
            )
            for (let i=0; i < data.report.length; i++){
                $('tbody#report').append(
                    '<tr><td>' + data.report[i].name + '</td>'
                    + '<td>' + data.report[i].diagnoses + '</td>'
                    + '<td>' + data.report[i].measure + '</td>'
                    + '<td>' + data.report[i].normal_value + '</td>'
                    + '<td>' + data.report[i].delta + '</td>'
                    + '<td>' + data.report[i].value + '</td>'
                    + '<td>' + data.report[i].description + '</td></tr>'
                )
            }
            $('.overlay_popup').hide().empty();
        })
        .fail(function(jqXHR, textStatus ) {
            $('.content').append(
                $('<div class="popup" style="display:block; position: absolute; top: 5vh;">' + textStatus + '</div>')
            )
            console.log('Error:', textStatus);
            $('.overlay_popup').hide();
        })
    })

    $('#save_btn').on('click', function() {
        $('.overlay_popup').show()
        $.ajax({
            url: 'predict/save/',
            method: 'post',
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(dotList),
            traditional: true,
            dataType: 'json'
        })
        .done(function(data) {
            console.log(data)
            $('.content').append(
                $('<div class="popup">Saved</div>')
                    .css('top', '5vh')
                    .css('width', '5vh')
                    .css('height', '1vh')
                    .css('text-align','center')
                    .css('display', 'block')
                    .css('overflow', 'hidden')
                    .css('position', 'absolute')
                    .css('left', '50%')
                    .fadeOut(2000)
            )
            $('.overlay_popup').hide().empty();
        })
        .fail(function(jqXHR, textStatus ) {
            $('.content').append(
                $('<div class="popup" style="display:block; position: absolute; top: 5vh;">' + textStatus + '</div>')
            )
            console.log('Error:', textStatus);
            $('.overlay_popup').hide();
        })
    })
});
