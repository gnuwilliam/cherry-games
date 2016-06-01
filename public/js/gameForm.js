class GameForm {
    constructor (formId, url) {
        this._formId = formId;
        this._url = url;
    }

    submit () {
        $.ajax({
            type: 'GET',
            url: this._url,
            data: $(`#${this._formId}`).serialize(),
            success: (data) => {
                this.success(data);
            }
        });
    }

    clean () {
        $('.result').empty();
    }

    success (data) {
        let self = this;

        self.clean();
        $('.result').append('<div class="loader"></div>');

        setTimeout(() => {
            self.clean();
            if (data.game) {
                $('.result').append(`<span><b>Game:</b> ${data.game}</span>`);
            }
            if (data.platform) {
                $('.result').append(`<span><b>Platform:</b> ${data.platform}</span>`);
            }
        }, 1000);
    }

    get formId () {
        return `#${this._formId}`;
    }
}
