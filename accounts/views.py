from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import SignupSerializer


@extend_schema(
    methods=["POST"],
    summary="회원가입 API",
    description="회원가입 요청을 처리하는 API입니다.",
    request=SignupSerializer,
    responses={
        status.HTTP_201_CREATED: OpenApiResponse(
            description="회원가입 성공",
            response=SignupSerializer,
            examples=[
                OpenApiExample(
                    name="sign up success response example",
                    value={
                        "username": "string",
                        "nickname": "string",
                        "roles": [{"role": "string"}],
                    },
                )
            ],
        ),
        status.HTTP_400_BAD_REQUEST: OpenApiResponse(
            description="잘못된 요청",
            response=SignupSerializer,
            examples=[
                OpenApiExample(
                    name="sign up fail response example",
                    value={
                        "username": ["This field is required."],
                        "password": ["This field is required."],
                        "nickname": ["This field is required."],
                    },
                )
            ],
        ),
    },
)
@api_view(["POST"])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
