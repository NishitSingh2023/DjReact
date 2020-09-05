import React from 'react';
import axios from 'axios';
import { Card, Button } from 'antd';
import CustomForm from '../components/Form';

class ArticleDetail extends React.Component {

    state = {
        article: {}             // only one obj
    }

    componentDidMount(){            //predifined func
        const articleID = this.props.match.params.articleID

        axios.get(`http://127.0.0.1:8000/api/${articleID}`)
        .then(res => {
          this.setState({
            article: res.data
          });
        
        })
    }

    handleDelete = (event) => {
        const articleID = this.props.match.params.articleID

        axios.delete(`http://127.0.0.1:8000/api/${articleID}`);
        this.props.history.push('/'); //to throw user back to home
    }

    render() {
        return(
            <div>
                <Card title= {this.state.article.title}>
                    <p>
                        {this.state.article.content}
                    </p>
                </Card>
                <br/>
                <CustomForm requestType = "put" articleID = {this.props.match.params.articleID} btnText="Update"/>
                <form onSubmitCapture= {this.handleDelete}>
                    <Button type="primary" htmlType="submit" danger>Delete</Button>
                </form>
            </div>
        )
    }
}

export default ArticleDetail;
