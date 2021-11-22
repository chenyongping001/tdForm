// app.js
App({
  onLaunch() {},

  getSession: function () {
    const that = this
    return new Promise(function (resolve, reject) {
      wx.login({
        success: res => {
          if (res.code) {
            wx.request({
              url: `${that.globalData.BASEURL}/wxauth/${res.code}`,
              success: function (res) {
                if (res.statusCode === 200) {
                  let session = res.data.session
                  that.globalData.session=session
                  resolve(session) //Promise成功的数据传递
                }
              }
            })
          } else {
            console.log('获取用户登录态失败！' + res.errMsg)
          }
        },
      })
    })
  },

  globalData: {
    session: null,
    BASEURL: 'https://www.tzpp.org/tdform',
  }
})