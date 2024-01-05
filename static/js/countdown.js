


$('[data-countdown]').each(function () {
    
    var $this = $(this),
        finalDate = $(this).data('countdown');
    if (!$this.hasClass('countdown-full-format')) {
        $this.countdown(finalDate, function (event) {
            $this.html(event.strftime('<span class="countdown-time"><span>%D</span><small>روز</small></span> <span class="countdown-time"><span>%H</span><small>ساعت</small></span> <span class="countdown-time"><span>%M</span><small>دقیقه</small></span> <span class="countdown-time"><span>%S</span><small>ثانیه</small></span>'));
        });
    } else {
        $this.countdown(finalDate, function (event) {
            $this.html(event.strftime('<span class="countdown-time"><span>%D</span><small>روز</small></span> <span class="countdown-time"><span>%H</span><small>ساعت</small></span> <span class="countdown-time"><span>%M</span><small>دقیقه</small></span> <span class="countdown-time"><span>%S</span><small>ثانیه</small></span>'));
        });
    }
});