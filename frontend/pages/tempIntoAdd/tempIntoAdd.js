// pages/tempIntoAdd/tempIntoAdd.js
import WxValidate from "../../utils/wxValidate"
Page({

  /**
   * 页面的初始数据
   */
  data: {
    name: "",
    idcard: "",
    outCompany: "",
    project: "",
    reason: "",
    note: "",
    contact: "",
    contactPhone: "",
    files: [],
    isHealth: ['是', '否'],
    days: ['1 天', '2 天', '3 天'],
    isOutProvince: ['否', '是'],
    healthValue: 0,
    daysValue: 0,
    outProvinceValue: 0,
  },
  onNameInput(e){
    this.setData({name:e.detail.value})
  },
  onIdcardInput(e){
    this.setData({idcard:e.detail.value})
  },
  onOutcompanyInput(e){
    this.setData({outCompany:e.detail.value})
  },
  onProjectInput(e){
    this.setData({project:e.detail.value})
  },
  onReasonInput(e){
    this.setData({reason:e.detail.value})
  },
  onNoteInput(e){
    this.setData({note:e.detail.value})
  },
  onContactInput(e){
    this.setData({contact:e.detail.value})
  },
  onContactphoneInput(e){
    this.setData({contactPhone:e.detail.value})
  },
  chooseImage: function (e) {
    var that = this;
    wx.chooseImage({
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: function (res) {
        // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        that.setData({
          files: that.data.files.concat(res.tempFilePaths)
        });
      }
    })
  },
  previewImage: function (e) {
    wx.previewImage({
      current: e.currentTarget.id, // 当前显示图片的http链接
      urls: this.data.files // 需要预览的图片http链接列表
    })
  },
  bindHealthChange: function (e) {
    this.setData({
      healthValue: e.detail.value
    })
  },
  bindDaysChange: function (e) {
    this.setData({
      daysValue: e.detail.value
    })
  },
  bindOutProvinceChange: function (e) {
    this.setData({
      outProvinceValue: e.detail.value
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.initValidate()
  },
  initValidate() {
    const rules = {
      name: {
        required: true,
        maxlength: 10
      },
      idcard: {
        required: true,
        idcard: true
      },
      outCompany: {
        required: true,
      },
      contact: {
        required: true,
        maxlength: 10
      },
      contactPhone: {
        required: true,
        tel: true
      }
    }
    const messages = {
      name: {
        required: "请输入入厂人员姓名",
        maxlength: "请输入正确的姓名"
      },
      idcard: {
        required: "请输入身份证号",
      },
      outCompany: {
        required: "请输入外包单位名称",
      },
      contact: {
        required: "请输入电厂联系人姓名",
        maxlength: "请输入正确的电厂联系人姓名"
      },
      contactPhone: {
        required: "请输入电厂联系人手机号码",
      }
    }
    this.wxValidate = new WxValidate(rules, messages)
  },

  formSubmit(e) {
    console.log(this.data)
    const params = e.detail.value
    // 传入表单数据，调用验证方法
    if (!this.wxValidate.checkForm(params)) {
      const error = this.wxValidate.errorList[0]
      wx.showToast({
        title: error.msg,
        icon: 'none',
        duration: 2000
      })
      return false
    }

    const count = this.data.files.length
    let msg = ""
    if (count < 3) {
      msg = '必须上传包含身份证|健康码|行程轨迹截图的附件资料,14天内有外省经历人员还需提供核酸检测报告!'
    } else if (count > 5) {
      msg = '不要上传过多图片!'
    }
    if (msg) {
      wx.showToast({
        title: msg,
        icon: 'none',
        duration: 5000
      })
      return false
    }

  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})